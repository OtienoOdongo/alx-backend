const createPushNotificationsJobs = require('./8-job');
const kue = require('kue');
const { expect } = require('chai');

describe('createPushNotificationsJobs', () => {
    before(() => queue.testMode.enter());
    afterEach(() => queue.testMode.clear());
    after(() => queue.testMode.exit());

    it('displays an error message if jobs is not an array', () => {
        const invalidJob = {
            phoneNumber: '+254789635538',
            message: 'Code 34623 Tests whether account is correctly verified',
        };
        expect(() => createPushNotificationsJobs(invalidJob, queue))
        .to.throw(Error, 'Jobs is not an array');
    });

    it('creates two new jobs to the queue', () => {
        const jobs = [
            {
                phoneNumber: '+2547091235489',
                message: 'Code 38965 Tests whether account is correctly verified',
            },
            {
                phoneNumber: '+254719876543211',
                message: 'Code 095679 Tests whether account is correctly verified',
            },
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(2);

        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal({
            phoneNumber: '+254711549085',
            message: 'Code 00243654 Tests whether account is correctly verified',
        });

        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].data).to.deep.equal({
            phoneNumber: '+254715237899',
            message: 'Code 905629 Tests whether account is correctly verified',
        });
    });
});

