# Multi-Runtime Containerized CI/CD Pipeline

A production-grade DevOps engineering project demonstrating automated container orchestration, multi-version runtime validation, and structured state management using **GitHub Actions** and **Docker Hub**.

## 🏗️ Architecture Overview

This pipeline transitions away from traditional bare-host testing by leveraging infrastructure-level guest containers. It automatically builds, secures, validates, and logs execution metrics across parallel execution environments.

```mermaid
graph TD
    A[Push to Main Branch] --> B[Job 1: Build & Ship]
    
    subgraph Job 1: Build & Ship Matrix
        B --> B1[Build Python 3.10 Image]
        B --> B2[Build Python 3.11 Image]
        B --> B3[Build Python 3.12 Image]
    end
    
    B1 & B2 & B3 -->|Push Tags| C[Docker Hub Registry]
    C -->|Trigger Dependency| D[Job 2: Test Container]
    
    subgraph Job 2: Test Container Matrix
        D --> D1[Run Guest Container 3.10]
        D --> D2[Run Guest Container 3.11]
        D --> D3[Run Guest Container 3.12]
        
        D1 --> E1[Parse Logs & Export Output]
        D2 --> E2[Parse Logs & Export Output]
        D3 --> E3[Parse Logs & Export Output]
    end
    
    E1 & E2 & E3 -->|Upload log files| F[GitHub Artifacts Storage]
    E1 & E2 & E3 -->|Pass JSON variable maps| G[Job 3: Print Metric Matrix]
    
    subgraph Job 3: Print Metric Summary
        G --> G1[Display 3.10 Lines]
        G --> G2[Display 3.11 Lines]
        G --> G3[Display 3.12 Lines]
    end
    
    G1 & G2 & G3 --> H[Broadcast Deployment Status]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style F fill:#bfb,stroke:#333,stroke-width:2px
    style H fill:#fbb,stroke:#333,stroke-width:2px