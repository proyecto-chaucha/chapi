# CHAPI
Chaucha API

## Requerimientos

- [Electrumx](https://github.com/proyecto-chaucha/electrumx)
- Configuración txindex=1 y server=1 (JSON-RPC) de [Chauchera](https://github.com/proyecto-chaucha/chauchera)

## Funcionamiento

```
$ pipenv run uvicorn chapi.main:app --reload --port 8080
```