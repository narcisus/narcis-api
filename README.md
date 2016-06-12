# narcis-api
The core API module for metadata about build screenshots

![narc-icon](https://cloud.githubusercontent.com/assets/3108007/12870500/752bd720-cd0d-11e5-988c-30d0ec386402.png)

## Dependencies

 - Python >=2.7
 - pip
 - `pip install -r requirements.txt`

## Setup

Create a config file and modify as desired.

```sh
cp narcis_api/config.example.py narcis_api/config.py
```

Initialize a database.

```sh
python create_db.py
```

 > TODO: Start flask app.

## Testing

```sh
python test.py
```
