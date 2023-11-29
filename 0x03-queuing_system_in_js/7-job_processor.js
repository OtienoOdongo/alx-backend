const kue = require('kue');
const queue = kue.createQueue();


const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    const totalProgress = 100;

    job.progress(0, totalProgress);

    if (blacklistedNumbers.includes(phoneNumber)) {
        done(Error(`Phone number ${phoneNumber} is blacklisted`));
        return;
    }

    job.progress(50, totalProgress);
    console.log(
        `Sending notification to ${phoneNumber}, with message: ${message}`
    );
    done();
}

const notificationQueue = kue.createQueue();
const queueName = 'push_notification_code_2';

notificationQueue.process(queueName, 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});

