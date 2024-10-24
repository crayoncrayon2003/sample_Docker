import docker
import time

IMAGE_NAME='hello-world:latest'
CONTAINER_NAME='my-hello-world'

def main():
    # get docker client
    client = docker.from_env()

    # pull image
    image = client.images.pull(IMAGE_NAME)
    time.sleep(5)

    print("-- image info --")
    print("image id   : ", image.id)
    print("image tags : ", image.tags)

    # get containers info
    container = None
    try:
        container = client.containers.get(CONTAINER_NAME)
    except:
        pass

    if(container == None):
        # run containers
        container = client.containers.run(IMAGE_NAME,name=CONTAINER_NAME,detach=True)
        time.sleep(5)

    logs = container.logs()
    print("-- container logs --")
    print(logs.decode('utf-8'))

    print("-- container info --")
    print("container id   : ", container.id)
    print("container id   : ", container.status)

    # stop containers
    container.stop()
    time.sleep(5)

    # remove images
    client.images.remove(image=IMAGE_NAME, force=True)

if __name__ == '__main__':
    main()