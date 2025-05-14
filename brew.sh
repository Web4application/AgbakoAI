sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker

ssh -i path/to/your-key.pem ubuntu@your-ec2-ip
docker build -t agbakoai-backend .
docker run -d -p 5000:5000 --name agbakoai-backend agbakoai-backend
curl http://localhost:5000

cd /path/to/frontend
vercel login
vercel deploy

sudo apt install certbot -y
sudo apt install python3-certbot-nginx -y

sudo certbot --nginx -d webapp4.com -d www.webapp4.com

https://webapp4.com
