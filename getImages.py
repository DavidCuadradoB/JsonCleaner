import requests
import properties.prop as prop


print ("keeeeey", prop.key)

response = requests.get("https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=CnRtAAAATLZNl354RwP_9UKbQ_5Psy40texXePv4oAlgP4qNEkdIrkyse7rPXYGd9D_Uj1rVsQdWT4oRz4QrYAJNpFX7rzqqMlZw2h2E2y5IKMUZ7ouD_SlcHxYq1yL4KbKUv3qtWgTK0A6QbGh87GB3sscrHRIQiG2RrmU_jF4tENr9wGS_YxoUSSDrYjWmrNfeEHSGSc3FyhNLlBU&key=AIzaSyBTy581iUctC_BM7NdMBjS-mcLMk_suq-8")

if response.history:
    print ("Request was redirected")
    for resp in response.history:
        print (resp.status_code, resp.url)
    print ("Final destination:")
    print (response.status_code, response.url)
else:
    print ("Request was not redirected")