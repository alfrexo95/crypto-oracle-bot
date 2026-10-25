# 🔮 GitHub Crypto Oracle Bot

Bot público que responde a issues con arte ASCII determinista, chistes y frases zen para traders.
Desbloquea **profecías premium** con pago en ETH verificado on-chain vía Etherscan.

## Cómo usarlo

1. **Abre un issue** → el Oracle responde gratis con arte ASCII + chiste + frase zen.
2. **Comenta lo que quieras** → el Oracle susurra una nueva profecía.
3. **Premium (0.50 USD)**: envía ETH a:
   `0xA5E6eB31868A85127B1ED82b8C760193356206ED`
   y comenta `/premium <tu_tx_hash>` → profecía extendida verificada on-chain.

## Stack
- GitHub Actions (`oracle.yml`)
- Python 3.11 + `requests`
- Etherscan API para verificación de pagos on-chain

## ¿Por qué es único?
- **Determinista pero único**: cada usuario + issue genera un arte distinto vía SHA-256.
- **Sin base de datos**: el estado vive en el propio issue.
- **Verificación real on-chain**: consulta Etherscan antes de entregar la premium.
