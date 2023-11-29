import redis from 'redis';

const client = redis.createClient({
  port: 6379,
  host: 'localhost',
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const handleMessage = (message) => console.log(message);

// Subscribe to the 'holberton school channel'
client.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
client.on('message', (channel, message) => {
  // Check if the message is received on the correct channel
  if (channel === 'holberton school channel') {
    // Check if the received message is 'KILL_SERVER'
    if (message === 'KILL_SERVER') {
      // Unsubscribe from the channel and quit the connection
      client.unsubscribe();
      client.quit();
    }

    // Handle the message by logging it to the console
    handleMessage(message);
  }
});

