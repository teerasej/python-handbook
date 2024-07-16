
# Create Sentry Account

In this exercise, you will create a Sentry account and set up a new project to monitor the performance of your Django application.

## Task 1: Create a Sentry account

1. Open a web browser and go to [Sentry](https://sentry.io/welcome/).
2. Click on the `Sign up` button to create a new account.
3. Fill in the required information and click on the `Sign up` button.
4. Verify your email address to complete the registration process.
5. Once you have verified your email address, you will be redirected to the Sentry dashboard.

## Task 2: Create a new project in Sentry

1. In the Sentry dashboard, click on the `Create Project` button.
2. Select the platform for your project, this time we will select `Django`.
3. In 'Set your alert frequency', we will select **Alert me on every new issue**
4. Name your project and click on the `Create Project` button.
5. In the `Configure your SDK` section, you will see the DSN (Data Source Name) for your project. Copy this DSN as we will need it to configure Sentry in our Django application.

### Example

```python
# settings.py
import sentry_sdk

sentry_sdk.init(
    dsn="https://xxxxxxxx.ingest.us.sentry.io/xxxxxxxxxxx",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
```