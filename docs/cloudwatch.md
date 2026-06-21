# AWS CloudWatch Monitoring

## Overview

CloudWatch is used to monitor AWS EC2 infrastructure and generate alerts when system health degrades.

## Monitored Metrics

- CPU Utilization
- Disk Usage
- Memory Usage
- Network Traffic

## Alerting

Amazon SNS is integrated with CloudWatch alarms.

### Notifications

- CPU > 80%
- Disk Usage > 80%
- Instance Status Check Failure

### Delivery Channel

- Email Notifications via Amazon SNS

## Benefits

- Real-time infrastructure visibility
- Automated incident detection
- Proactive alerting
- Improved operational reliability