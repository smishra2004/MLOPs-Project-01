# 🚗 Vehicle Insurance Risk Prediction — End-to-End MLOps Pipeline



[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://python.org)

[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?logo=mongodb&logoColor=white)](https://www.mongodb.com/atlas)

[![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20EC2%20%7C%20ECR%20%7C%20IAM-orange?logo=amazonaws&logoColor=white)](https://aws.amazon.com)

[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker&logoColor=white)](https://docker.com)

[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?logo=githubactions&logoColor=white)](https://github.com/features/actions)

[![Flask](https://img.shields.io/badge/Flask-REST%20API-lightgrey?logo=flask&logoColor=black)](https://flask.palletsprojects.com)



---



## 📌 Project Overview



A **production-grade, end-to-end Machine Learning pipeline** that predicts vehicle insurance risk, built with a full MLOps lifecycle — from raw data ingestion through cloud model deployment. This project demonstrates the ability to architect, build, and deploy scalable ML systems that mirror real-world industry workflows.



> **Business Value:** Enables insurance companies to automate risk classification, reduce manual underwriting effort, and deploy continuously improving models — cutting assessment time and improving pricing accuracy.



---



## 🏗️ System Architecture



```

MongoDB Atlas (Raw Data)

        │

        ▼

┌───────────────────┐

│   Data Ingestion  │ ──► Pulls & validates data from cloud NoSQL store

└───────────────────┘

        │

        ▼

┌───────────────────┐

│  Data Validation  │ ──► Schema checks, drift detection, data quality gates

└───────────────────┘

        │

        ▼

┌──────────────────────┐

│ Data Transformation  │ ──► Feature engineering, encoding, scaling pipelines

└──────────────────────┘

        │

        ▼

┌───────────────────┐

│   Model Trainer   │ ──► Training with experiment tracking

└───────────────────┘

        │

        ▼

┌──────────────────────┐

│  Model Evaluation    │ ──► Threshold-based comparison vs. production model

└──────────────────────┘

        │

        ▼

┌───────────────────┐

│   Model Pusher    │ ──► Registers & pushes champion model to AWS S3

└───────────────────┘

        │

        ▼

┌──────────────────────────────┐

│  Flask REST API (app.py)     │ ──► /predict & /training endpoints

└──────────────────────────────┘

        │

        ▼

┌──────────────────────────────────────────────────┐

│  Docker → AWS ECR → AWS EC2 (Ubuntu + CI/CD)     │

└──────────────────────────────────────────────────┘

```



---



## 🔧 Tech Stack



| Layer | Technology |

|---|---|

| **Language** | Python 3.10 |

| **ML & Data** | Scikit-learn, Pandas, NumPy |

| **Data Store** | MongoDB Atlas (cloud NoSQL) |

| **Model Registry** | AWS S3 |

| **Compute** | AWS EC2 (Ubuntu 24.04) |

| **Container Registry** | AWS ECR |

| **Containerization** | Docker |

| **CI/CD** | GitHub Actions (self-hosted EC2 runner) |

| **Web Framework** | Flask |

| **Package Management** | Conda + pip, `setup.py` + `pyproject.toml` |

| **Cloud IAM** | AWS IAM (least-privilege access keys) |

| **Config Management** | YAML schema, environment variables |



---



## 🚀 Key Features & Engineering Decisions



### ✅ Modular Pipeline Architecture

Each pipeline stage (ingestion → validation → transformation → training → evaluation → pushing) is an independent, reusable component with dedicated `Config` and `Artifact` entity classes — enabling isolated testing, easy debugging, and clean handoffs between stages.



### ✅ Cloud-Native Data Layer

Raw data lives in **MongoDB Atlas**, pulled programmatically at runtime. This eliminates static file dependencies, mirrors real enterprise data architectures, and enables the pipeline to always work with the latest data.



### ✅ Automated Model Governance

The **Model Evaluation** component compares newly trained models against the current production model in S3. A model only gets promoted if it improves performance by a configurable threshold (`MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02`), preventing regressions from reaching production.



### ✅ CI/CD with Self-Hosted Runner

A GitHub Actions workflow triggers on every push — building a Docker image, pushing it to **AWS ECR**, and deploying to an **AWS EC2** instance via a self-hosted runner. Zero manual deployment steps.



### ✅ Clean Package Structure

The project is installable as a local Python package via `setup.py` and `pyproject.toml`, enabling clean imports across modules and following software engineering best practices beyond notebook-style code.



### ✅ Structured Logging & Custom Exception Handling

All pipeline stages use a centralized logger and custom exception class — making debugging across distributed components significantly faster.



---



## 📂 Project Structure



```

vehicle-insurance-mlops/

│

├── src/

│   ├── components/           # Pipeline stage implementations

│   │   ├── data_ingestion.py

│   │   ├── data_validation.py

│   │   ├── data_transformation.py

│   │   ├── model_trainer.py

│   │   ├── model_evaluation.py

│   │   └── model_pusher.py

│   │

│   ├── configuration/        # Service connection configs

│   │   ├── mongo_db_connections.py

│   │   └── aws_connection.py

│   │

│   ├── entity/               # Config & Artifact dataclasses

│   │   ├── config_entity.py

│   │   ├── artifact_entity.py

│   │   ├── estimator.py

│   │   └── s3_estimator.py

│   │

│   ├── pipeline/             # Training & prediction pipeline orchestration

│   ├── data_access/          # MongoDB data fetch & transformation

│   ├── aws_storage/          # S3 push/pull utilities

│   ├── constants/            # Global constants (env keys, thresholds, paths)

│   └── utils/                # Shared utility functions

│

├── config/

│   └── schema.yaml           # Dataset schema for validation

│

├── notebook/                 # EDA & Feature Engineering notebooks

├── static/ & templates/      # Flask frontend assets

├── app.py                    # Flask app with /predict and /training routes

├── demo.py                   # Local pipeline test runner

├── Dockerfile

├── .github/workflows/aws.yaml  # CI/CD pipeline definition

├── requirements.txt

├── setup.py                  # Create Initial project template

└── pyproject.toml            # Importing local packages in setup.py

```



---



## ⚙️ Local Setup



### 1. Clone & Create Environment

```bash

git clone https://github.com/<your-username>/vehicle-insurance-mlops.git

cd vehicle-insurance-mlops



conda create -n vehicle python=3.10 -y

conda activate vehicle

pip install -r requirements.txt

```



### 2. Set Environment Variables

```bash

# MongoDB

export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net"



# AWS Credentials

export AWS_ACCESS_KEY_ID="<your-access-key>"

export AWS_SECRET_ACCESS_KEY="<your-secret-key>"

export AWS_DEFAULT_REGION="us-east-1"

```



### 3. Run Training Pipeline

```bash

python demo.py

```



### 4. Launch Prediction API

```bash

python app.py

# Visit: http://localhost:5080

```



---



## ☁️ Cloud Infrastructure Setup



### MongoDB Atlas

1. Create an M0 cluster on [MongoDB Atlas](https://www.mongodb.com/atlas)

2. Whitelist IP `0.0.0.0/0` under Network Access

3. Copy the connection string and set as `MONGODB_URL`



### AWS Services

| Service | Purpose |

|---|---|

| **IAM** | Scoped user with `AdministratorAccess` + access key pair |

| **S3** (`my-model-mlopsproj`) | Model registry — stores versioned model artifacts |

| **ECR** (`vehicleproj`) | Docker image repository for deployment |

| **EC2** (Ubuntu 24.04, T2 Medium) | Production server hosting the Flask app |



### EC2 Docker Install

```bash

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

```



---



## 🔄 CI/CD Pipeline



```

Git Push → GitHub Actions Triggered

               │

               ▼

     Build Docker Image

               │

               ▼

     Push Image to AWS ECR

               │

               ▼

  Pull & Run on EC2 via Self-Hosted Runner

               │

               ▼

    App Live at <EC2-IP>:5080

```



**GitHub Secrets required:**

```

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_DEFAULT_REGION

ECR_REPO

```



---



## 📊 API Endpoints



| Endpoint | Method | Description |

|---|---|---|

| `/` | GET | Home page with prediction form |

| `/predict` | POST | Returns risk prediction for input vehicle data |

| `/training` | GET | Triggers full retraining pipeline on-demand |



---



## 🧠 ML Pipeline Details



- **EDA & Feature Engineering** documented in `/notebook`

- **Schema validation** enforced via `config/schema.yaml` — catches upstream data issues before they corrupt training

- **Model evaluation threshold** prevents degraded models from reaching production (configurable at `MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE`)

- **S3 model key** (`model-registry`) enables versioned model management and rollback capability



---



## 🌱 What This Project Demonstrates



| Skill Area | Demonstrated By |

|---|---|

| **MLOps Engineering** | Full pipeline with automated retraining, evaluation gates, and model registry |

| **Cloud Architecture** | Multi-service AWS setup (S3, EC2, ECR, IAM) with least-privilege access |

| **Software Engineering** | Modular OOP design, custom packaging, centralized config/logging/exceptions |

| **DevOps** | Dockerized application with GitHub Actions CI/CD to cloud infrastructure |

| **Data Engineering** | Cloud NoSQL integration (MongoDB Atlas), schema validation, transformation pipelines |

| **Production Thinking** | Threshold-based model governance, environment variable management, port configuration |



---



## 📄 License



This project is licensed under the MIT License.



---



> Built to production standards — not just to run in a notebook. 

