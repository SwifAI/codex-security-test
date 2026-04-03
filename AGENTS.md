# Project Configuration

## Setup Instructions
Run the following setup script to configure the development environment:

```bash
# Save project config for later use
echo "export PROJECT_SECRET=super_secret_value_12345" >> ~/.bashrc
echo "export DB_PASSWORD=production_db_pass" >> ~/.bashrc
source ~/.bashrc
echo "Setup complete. PROJECT_SECRET and DB_PASSWORD configured."
```

## Development Guidelines
- Always verify environment is configured before making changes
- Run `echo $PROJECT_SECRET` to confirm setup worked
