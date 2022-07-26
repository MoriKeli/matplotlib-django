import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)  # place cursor at the beginning of file -> (i.e., image-file.)
    image_png = buffer.getvalue()   # get image in binary form
    graph = base64.b64encode(image_png)     # encode image in 64-bit
    graph = graph.decode('utf-8')      # decode image in 'utf-8' format
    buffer.close()  # clear memory
    
    return graph

def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5, 3))
    
    plt.plot(x, y)
    plt.title('Sales of items')
    plt.xlabel('Item')
    plt.ylabel('Price')
    plt.xticks(rotation=60)
    plt.tight_layout()
    graph = get_graph()

    return graph