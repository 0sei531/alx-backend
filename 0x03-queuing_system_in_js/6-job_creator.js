import kue from 'kue';

// Create a Kue queue instance
const queue = kue.createQueue();

// Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is the code to verify your account',
};

// Define the queue name
const queueName = 'push_notification_code';

// Create and save the job
const job = queue.create(queueName, jobData)
  .save((err) => {
    if (err) {
      console.error(`Error creating job: ${err}`);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Attach event listeners for job completion and failure
job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (err) => {
  console.log(`Notification job failed: ${err}`);
});
