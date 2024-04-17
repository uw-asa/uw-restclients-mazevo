# REST client for the Mazevo API

Installation:

    pip install uw-restclients-mazevo

To use this client, you'll need these settings in your application or script:

    # Specifies whether requests should use live or mocked resources,
    # acceptable values are 'Live' or 'Mock' (default)
    RESTCLIENTS_MAZEVO_DAO_CLASS='Live'

    # API key
    RESTCLIENTS_MAZEVO_API_KEY='...'

    # Mazevo API URL prefix
    RESTCLIENTS_MAZEVO_HOST='https://...mymazevo.com'

Optional settings:

    # Customizable parameters for urllib3
    RESTCLIENTS_MAZEVO_TIMEOUT=60
    RESTCLIENTS_MAZEVO_POOL_SIZE=10
