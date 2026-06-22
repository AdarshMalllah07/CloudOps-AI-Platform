import subprocess

def restart_deployment():
    subprocess.run([
        "kubectl",
        "rollout",
        "restart",
        "deployment/cloudops-app",
        "-n",
        "cloudops"
    ])

def scale_deployment(replicas):
    subprocess.run([
        "kubectl",
        "scale",
        f"--replicas={replicas}",
        "deployment/cloudops-app",
        "-n",
        "cloudops"
    ])