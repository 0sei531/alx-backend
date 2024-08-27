import kue from 'kue';

// Create a Kue queue instance
const queue = kue.createQueue();

// Define the function to send notifications
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Define the job processing logic
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  
  // Call the function to send the notification
  sendNotification(phoneNumber, message);
  
  // Indicate that the job is complete
  done();
});

// Handle queue errors
queue.on('error', (err) => {
  console.error(`Queue error: ${err}`);
});
