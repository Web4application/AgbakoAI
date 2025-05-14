# Example of integrating elFinder into your project
git clone https://github.com/Studio-42/elFinder.git

rsync -avz /var/www/html/ user@backup_server:/path/to/backup/

mkdir web4-cpanel
cd web4-cpanel
mkdir backend
cd backend
npm init -y
npm install express mysql2 bcryptjs jsonwebtoken dotenv
