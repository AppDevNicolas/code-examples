from datetime import datetime


def convert_seconds_to_hms(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def convert_seconds_to_dhms(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return "%d days, %d hours, %d minutes, %d seconds" % (days, hours, minutes, seconds)


def convert_to_seconds_since_midnight(seconds):
    # Get the current datetime
    now = datetime.now()
    # Calculate the start of the current day
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)

    seconds_since_epoch_midnight = start_of_day.timestamp()

    # Calculate the difference in seconds
    seconds_since_midnight = (seconds - seconds_since_epoch_midnight)
    return seconds_since_midnight


def convert_datetime_to_str_ISO_8601_with_Z(dt):
    # Format the datetime object to the desired string format
    utc_string = dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    return utc_string
