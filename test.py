import graphviz
from PIL import Image
import io

dot = """
# Sample Title

This is a **Markdown** paragraph with _some_ formatting.

- Bullet 1
- Bullet 2
"""

# Create graph from dot source
graph = graphviz.Source(dot, format="png")
img_bytes = graph.pipe()

# Convert to PIL Image
image = Image.open(io.BytesIO(img_bytes))
image.show()  # or use it as a PIL object
