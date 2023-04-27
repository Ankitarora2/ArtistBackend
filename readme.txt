The API endpoints for the views defined in the provided code:

WorkList: This is a GET endpoint that returns a list of all works available in the database. The endpoint supports filtering by work_type and artist name through query parameters.

Endpoint: /works/
Supported HTTP methods: GET
Query parameters:
work_type: Filter works by work type
artist: Filter works by artist name
ArtistList: This is a GET endpoint that returns a list of all artists available in the database.

Endpoint: /artists/
Supported HTTP methods: GET
WorkCreate: This is a POST endpoint that creates a new work for the authenticated user (assuming the user is an artist). The endpoint expects a JSON payload containing the link and work_type fields.

Endpoint: /works/create/
Supported HTTP methods: POST
Payload: JSON object containing link and work_type fields.
register: This is a POST endpoint that creates a new client user in the database. The endpoint expects a JSON payload containing the name, username, and password fields.

Endpoint: /register/
Supported HTTP methods: POST
Payload: JSON object containing name, username, and password fields.
