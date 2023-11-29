const kue = require('kue');
const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
  phoneNumber: '+254723458905',
  message: 'Kindly verify the details this account.',
};

// Create a job in the push_notification_code queue
const notificationJob = queue
  .create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${notificationJob.id}`);
    } else {
      console.error(`Error creating notification job: ${err.message}`);
    }
  });

// Event listener for job completion
notificationJob.on('complete', () => {
  console.log('Notification job completed');
});

// Event listener for job failure
notificationJob.on('failed', (errorMessage) => {
  console.error(`Notification job failed: ${errorMessage}`);
});

