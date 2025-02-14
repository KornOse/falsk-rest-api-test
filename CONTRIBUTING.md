# Contributing

## How to run the Dockerfile locally

```
docker run -dp 5000:5000 -w //app -v "$(Get-Location)://app" flask-smorest-api "flask run --host 0.0.0.0"
```