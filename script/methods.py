import docker

def check_into_DockerHub(image):
    client = docker.from_env()

    try:
        client.images.get_registry_data(image)
        client.images.pull(image)
        return "Image found and pulled successfully."
    except Exception as error:
        return str(error)      