const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

const app = express();
const port = 1245;

const client = redis.createClient();
const reserveSeatAsync = promisify(client.set).bind(client);
const getCurrentAvailableSeatsAsync = promisify(client.get).bind(client);

const queue = kue.createQueue();

let numberOfAvailableSeats = 50;
let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  res.json({ numberOfAvailableSeats: `${numberOfAvailableSeats}` });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (!err) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      const currentAvailableSeats = await getCurrentAvailableSeatsAsync('available_seats');
      if (currentAvailableSeats <= 0) {
        reservationEnabled = false;
        return done(new Error('Not enough seats available'));
      }

      numberOfAvailableSeats = currentAvailableSeats - 1;
      await reserveSeatAsync('available_seats', numberOfAvailableSeats);

      if (numberOfAvailableSeats === 0) {
        reservationEnabled = false;
      }

      console.log(`Seat reservation job ${job.id} completed`);
      done();
    } catch (error) {
      console.log(`Seat reservation job ${job.id} failed: ${error.message}`);
      done(error);
    }
  });
});

reserveSeatAsync('available_seats', numberOfAvailableSeats);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

