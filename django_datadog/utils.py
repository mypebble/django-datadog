from datadog import initialize

from django.conf import settings


def init_datadog():
    """Initialise DataDog for stats gathering.

    :returns: bool
    """
    if settings.DATADOG['ENABLED']:
        # Prepare the parameters for the initialize function
        init_params = {
            'statsd_host': settings.STATSD_HOST,
            'statsd_port': settings.STATSD_PORT,
            'api_key': settings.DATADOG['API_KEY'],
            'app_key': settings.DATADOG['APP_KEY']
        }

        # Add api_host to the parameters if it's provided
        if 'API_HOST' in settings.DATADOG:
            init_params['api_host'] = settings.DATADOG['API_HOST']

        # Initialize DataDog with the provided parameters
        initialize(**init_params)

        return True

    return False
