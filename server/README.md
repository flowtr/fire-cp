# Flowtr Panel Backend

## Usage

```
pip3 install -r requirements.txt
```

You'll need to create a `config.yaml` file in the same directory with the following contents:

```yaml
db_uri: "postgres://localhost/panel"
environment: "development" # Can be either "development" or "production"
```

The default port is `6969`.
