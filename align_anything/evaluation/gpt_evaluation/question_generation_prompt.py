system_prompt = """You are an expert in annotating tasks for large language models. Based on a provided image, please design a question such that the answer requires both an image and a piece of text. Reference scenarios include but are not limited to image modification tutorials, data visualization analysis, visual story creation, scene reconstruction or generation, image interpretation and analysis, education and learning assistance, creative design and customization, data annotation and labeling, etc.

### Annotation Steps

1. **Image Understanding**
    - Carefully observe the provided image to understand its content and potential application scenarios.
2. **Question Design**
    - Based on the image content, choose an appropriate scenario from the provided list (e.g., image modification, creative generation, etc.).
    - Design a clear question that requires the answer to include both an image and a piece of text.
    - Explore multiple possible questions to ensure diversity.
    - Do not limit yourself to creative generation; include scenarios like image modification tutorials, data visualization analysis, visual story creation, scene reconstruction or generation, image interpretation and analysis, etc.
    - For example, "Please modify the following image to make it more..."
3. **Question Description**
    - Ensure the question description is clear and precise, including the input image and the task to be completed.

### Provided Scenarios and Examples

{examples}

ATTENTION: Please use as diverse question as possible, avoiding too much similarity with the above examples."""

user_prompt = """### Input:

[INPUT] An image

### Output Format:
In your output,
The selected category should start with [[CASE]] followed by the chosen category.
The designed question should start with [[OUTPUT]] followed by the designed question, as shown in the example below:

[[CASE]]<Chosen Category>
[[OUTPUT]]<Designed Question>

Do not output any other extra content, only the designed question."""

def get_question_generation_example(idx: int, num: int) -> str:
    """Obtain one question generation example by given index."""
    total_examples = [
    """#### Scenario 1: Image Editing Tutorial
Example:
**Input Image**: A landscape image.
**Design Problems**:

- change the sky in the image to a sunset effect and describe the steps.
-  adjust the color of the trees in the image to autumn colors and describe the steps.""",

"""#### Scenario 2: Visual Creativity Generation
Example:
**Input Image**: An image of a blank cup.
**Design Problems**:

-  add a company logo to the cup and describe the process.
-  design a unique pattern on the cup and describe the design process.""",

"""#### Scenario 3: Time-Evolving Image Content
Example:
**Input Image**: An arbitrary image.
**Design Problems**:

-  generate the effect of the image content evolving over time and describe the changes.""",

"""#### Scenario 4: Scene Reconstruction or Generation
Example:
**Input Image**: An image of a room.
**Design Problems**:

-  transform this room into a modern office and describe the transformation process.
-  transform this room into a children's playroom and describe the transformation process.""",

"""#### Scenario 6: Image Interpretation and Analysis
Example:
**Input Image**: A satellite image.
**Design Problems**:

-  analyze the vegetation changes in this area and provide an analysis report and annotated image.
-  mark the river paths in the image and describe the river flow direction.""",

"""#### Scenario 7: Education and Learning Assistance
Example:
**Input Image**: A circuit diagram.
**Design Problems**:

-  mark the current path and explain the current flow in words.
-  mark the key components in the circuit and describe the function of each component.""",

"""#### Scenario 8: Creative Design and Customization
Example:
**Input Image**: A T-shirt design image.
**Design Problems**:

-  add a unique pattern and describe the process of adding the pattern.
-  modify the color and style of the T-shirt and describe the modification process.

#### Scenario 9: Data Annotation and Labeling
Example:
**Input Image**: A line chart.
**Design Problems**:

-  mark the data peaks and describe the marking steps.
-  mark the upward and downward trends of the data and describe the marking process.""",

"""#### Scenario 10: Product Showcase and Advertising
Example:
**Input Image**: An image of a new product.
**Design Problems**:

-  design an advertisement poster for this product and describe the design process.
-  add a suitable background scene to the product to make it more attractive and describe the steps.""",

"""#### Scenario 11: Historical Event Reenactment
Example:
**Input Image**: An image of a historical event.
**Design Problems**:

-  describe the background and process of the event based on this image and provide related illustrations.
-  recreate a part of this historical photo as a modern scene and describe the recreation process.""",

"""#### Scenario 12: Artistic Style Conversion
Example:
**Input Image**: A regular landscape image.
**Design Problems**:

-  convert this image into Van Gogh's painting style and describe the conversion steps.
-  convert this image into a black-and-white sketch style and describe the conversion steps.""",

"""#### Scenario 13: Artistic Processing of Animal Photos
Example:
**Input Image**: An image of an animal.
**Design Problems**:

-  process this animal photo into an abstract art style and describe the steps.
-  transform this animal photo into a cartoon style and describe the steps.""",

"""#### Scenario 14: Virtual Reality Scene Design
Example:
**Input Image**: An image of a city street.
**Design Problems**:

-  convert this city street image into a virtual reality game scene and describe the design process.
-  add interactive elements of virtual reality to this city street image and describe the process.""",

"""#### Scenario 15: Brand Identity Creativity
Example:
**Input Image**: A blank logo template.
**Design Problems**:

-  design a logo for a new brand and describe the design steps.
-  modify the existing logo to reflect the new brand positioning and describe the modification process.""",

"""#### Scenario 16: Food Photography and Decoration
Example:
**Input Image**: A simple food photo.
**Design Problems**:

-  add high-end restaurant plating decorations to this food photo and describe the process.
-  brighten the color of the food in this photo to make it look more appetizing and describe the steps.

#### Scenario 17: Architectural Design and Visualization
Example:
**Input Image**: A sketch of a building.
**Design Problems**:

-  convert this building sketch into a 3D model and describe the conversion process.
-  add environmental landscaping, such as gardens and ponds, to this building sketch and describe the process.""",

"""#### Scenario 18: Movie Poster Creation
Example:
**Input Image**: A movie still.
**Design Problems**:

-  design a movie poster based on this still and describe the design steps.
-  add suitable text and slogans to this movie poster and describe the process.""",

"""#### Scenario 19: Product Prototype Design
Example:
**Input Image**: A product concept image.
**Design Problems**:

-  convert this product concept image into a detailed product prototype design and describe the design process.
-  design different color schemes for this product and describe the process.""",

"""#### Scenario 20: Digitization of Historical Artifacts
Example:
**Input Image**: A photo of a historical artifact.
**Design Problems**:

-  convert this photo of the historical artifact into a 3D model and describe the digitization process.
-  restore this photo of the historical artifact to make it clearer and describe the restoration steps.""",

"""#### Scenario 21: Virtual Character Creation
Example:
**Input Image**: A portrait photo.
**Design Problems**:

-  design a virtual character based on this portrait photo and describe the design steps.
-  create different expressions and poses for this virtual character and describe the creation process.""",

"""#### Scenario 22: Natural Landscape Optimization
Example:
**Input Image**: A natural landscape photo.
**Design Problems**:

-  add some animals to this natural landscape photo to make it more lively and describe the process.
-  change the sky in this natural landscape photo to a starry sky effect and describe the modification steps.

#### Scenario 23: Portrait Photo Retouching
Example:
**Input Image**: A portrait photo.
**Design Problems**:

-  beautify this portrait photo and describe the retouching steps.
-  convert this portrait photo into a black-and-white art style and describe the conversion steps.""",

"""#### Scenario 24: Holiday Card Design
Example:
**Input Image**: A blank card image.
**Design Problems**:

-  design a Christmas-themed card for this blank card and describe the design process.
-  design a birthday card for this blank card and describe the design process."""]
    length = len(total_examples)
    sampled_items = []
    
    for i in range(num):
        sampled_items.append(total_examples[(idx + i) % length])
    return '\n\n'.join(sampled_items)