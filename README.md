# AWS-Flask Server Project

This project demonstrates practical DevOps and software engineering capabilities. It's a Flask server with AWS S3 integration, showing I can build and deploy cloud-connected applications.

## Core Features
- Flask HTTP server with multiple endpoints
- AWS S3 bucket management
- Error handling and logging
- Environment variable configuration

## Technical Stack -
- Python/Flask for backend
- AWS S3 for cloud storage
- Logging for monitoring
- Environment management

## Setup
1. Clone repo
2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Configure AWS credentials in ~/.aws/credentials
5. Start server:
```bash
python server.py
```

## Why This Matters
Modern software development demands cloud expertise. This project shows I can:
- Build RESTful APIs
- Integrate with AWS services
- Handle errors properly
- Structure a production-ready application

## APIs
- `/health` - Server health check
- `/aws-test` - AWS connectivity test
- `/create-bucket` - Create S3 bucket
- `/upload-test` - Test file upload
- `/read-file` - Read uploaded file
- `/list-files` - List bucket contents

## Future Enhancements
- Docker containerization
- CI/CD pipeline
- AWS Elastic Beanstalk deployment
- Enhanced monitoring

## Contact
Rapheal M. Suber


