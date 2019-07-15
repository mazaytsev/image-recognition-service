import numpy as np
from keras.preprocessing import image
from keras import backend as K
from keras.applications import imagenet_utils, VGG16

from service import service_utils


def process_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    p_img = imagenet_utils.preprocess_input(img_array)
    return p_img


def recognize_image(image_url, chat_id, client_ip):
    # path to image
    img_path = service_utils.download_image(str(image_url))

    # process the image
    pImg = process_image(img_path)

    K.clear_session()
    # define the vgg model
    vggnet = VGG16(weights='imagenet', include_top=True)

    # make predictions on test image using vgg
    prediction = vggnet.predict(pImg)

    # obtain the top-5 predictions
    results = imagenet_utils.decode_predictions(prediction)[0]

    # format results in normal way
    results_string = ''
    for i in range(results.__len__()):
        results_string += "{result_number}. \"{result_name}\" with chance {chance}%\n" \
            .format(result_number=i+1,
                    result_name=results[i][1].replace('_', ' ').title(),
                    chance=round(results[i][2] * 100, 2))
    K.clear_session()

    # send the results back
    service_utils.send_response(results_string, chat_id, client_ip)
