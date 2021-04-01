import requests

import vk
from vk_api import VkApi
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
import requests
from io import BytesIO

user_id = 186484422
group_id = 203658356
 
def main():
    res = requests.post('https://www.anilibria.tv/public/api/index.php', data={'query': "feed",'page':"1",'perPage':"1", 'filter': "names"})
    name = res.json()['data'][0]['release']['names'][0]

    release = res.json()['data'][0]['release']['id']
    res2 = requests.post('https://www.anilibria.tv/public/api/index.php', data={'query': "release",'id':release})
    image = "https://www.anilibria.tv/" + res2.json()['data']['poster']

    send(user_id, name, image)

def send(id, msg, img):
    import vk_api
    import requests

    attachments = []

    ses_req = requests.Session()

    session = VkApi(token='8fdf4fe1f59267d65bb0587f30a7f0adbe2315e2ae83731758e1f7208fc0ebc3a8b6834da89be3d187b87').get_api()

    upload = vk_api.VkUpload(session)

    image = ses_req.get(img, stream=True)

    photo = upload.photo_messages(photos=image.raw)[0]

    attachments.append(
                    'photo{}_{}'.format(photo['owner_id'], photo['id'])
                )

    session.messages.send(user_id=id, message=msg, v='5.103', random_id=0, attachment=attachments)
    #session.messages.send(user_id=id, message=msg, v='5.103', random_id=0)


if __name__ == '__main__':
    main()
