# Markov Chain Text Generator

This project is a **Markov Chain-based text generator** implemented in Python. It processes an input text file to build a probabilistic model of word sequences, allowing it to generate coherent, randomly constructed text that mimics the style of the source.

---

## Features

- **Markov Chain Graph**:
  - Builds a graph where:
    - **Vertices** represent unique words.
    - **Edges** represent transitions between words, weighted by their frequency in the input text.
  - Probability-based selection for the next word during text generation.

- **Customizable Text Generation**:
  - Configurable output length (default: 50 words).
  - Processes any text file for training the model.
  - Adds punctuation and formatting to make the output more natural.

- **Reusable Graph Structure**:
  - The graph structure can be used for various other Markov Chain-based applications.

---

## Project Structure

- **`MarkovChain.py`**  
  Contains the `Graph` and `Vertex` classes for building and managing the Markov Chain:
  - `Vertex`: Represents a word in the graph and stores its connections.
  - `Graph`: Manages vertices, edges, and probability mappings for the chain.

- **`Compose.py`**  
  Handles:
  - Text preprocessing (removal of punctuation and extra spaces).
  - Graph creation based on input text.
  - Randomized text generation using the Markov Chain.

- **`text.txt`**  
  Sample text file used as input for training the Markov Chain. Replace it with your own file to generate text in different styles.

---

## How to Use

### Prerequisites
- Python 3.6 or higher.

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sabdikay/Markov-Chain-Text-Generator.git
   cd markov-chain-text-generator
   ```

2. **Prepare Input**:
   - Replace the contents of `text.txt` with the text you want to use for training.

3. **Run the Program**:
   ```bash
   python Compose.py
   ```

4. **View Output**:
   - The program will display the generated text in the terminal.

---

## Example

**Input (`text.txt`)**:
```
**Sunset on the Frontier**

Dust swirled in a golden haze across the town's single dirt road as the scorching sun descended behind the ridge, painting the sky in hues of orange and crimson. Prescott Flats was a small, rugged settlement – a collection of sun-bleached wooden buildings, a battered saloon with swinging doors, and a lone church whose bell tolled at dawn and dusk.

Caleb “Coyote” Grady, a wiry drifter with a scar crossing his left cheek, reined in his weary horse, Daisy, beside the hitching post in front of the Rusty Spur Saloon. He was on a mission of sorts: to find a man named Harley Graves, rumored to be hiding out in these parts.

A hush fell inside the saloon as Caleb shouldered his way through the double doors. Oil lamps flickered along the walls, casting dancing shadows over patrons hunched at tables or seated at the bar. The barkeep, a barrel-chested fellow with a bristly mustache, watched from behind the counter. In the far corner, a weathered man strummed a melancholy tune on a guitar.

“Evenin’,” Caleb said, tipping his sweat-stained hat.

He slid onto a stool at the bar. A glass of whiskey was poured wordlessly, and Caleb took a sip. For a moment, he let the burn run through him, savoring the quiet tension in the room. Then he asked, “I hear Harley Graves might be passin’ through.”

A few folks shifted in their chairs, eyes darting anywhere but toward the drifter. After a long pause, the barkeep cleared his throat.

“He’s been around. Reckon he’s stayin’ up by the old Perkins homestead, coupla miles north,” the barkeep finally managed.

Caleb nodded and downed the rest of his whiskey. “Obliged,” he said, dropping a coin on the counter.

As he stepped outside, the last rays of light vanished beyond the horizon. The star-strewn sky enveloped the town in darkness, and lanterns flickered in windows up and down the street.

Caleb rode north, each hoofbeat echoing in the stillness of the desert evening. A soft breeze carried the scent of sagebrush and the distant howl of a coyote, reminding him of the harsh, lonely nature of the frontier. A small shack came into view, lit by a single lantern flickering on the porch.

He dismounted and crept closer. The wooden planks of the porch groaned under his boots. There, slumped in a rocker, a lean man in a dusty coat lifted his head. Beneath a wide-brimmed hat, pale eyes narrowed at the sight of Caleb.

“You must be Graves,” Caleb said quietly.

Harley Graves reached for the revolver at his hip, but in a blur, Caleb drew his own. A tense silence fell, broken only by the hiss of a desert breeze.

“Been lookin’ for you,” Caleb continued, not lowering his firearm. “Heard you’re tied to the robbery in Elms Creek. You left a trail of lead and a wounded deputy.”

Graves’s features hardened. “I’m guessin’ you aim to collect the bounty.”

“That’s how things work out here,” Caleb said, voice low.

Graves lunged, but before he could pull the trigger, Caleb fired. The shot rang in the night like thunder, and Graves’s revolver dropped to the porch with a clatter. Gravel crackled as he collapsed, blood staining the weathered boards.

Caleb holstered his smoking iron and crouched by the dying man. Graves tried to speak, but only a rattling breath escaped his lips. In the end, all that remained was the crackle of the lantern flame and the soft rustle of desert wind.

With a weary sigh, Caleb stood and looked at the lifeless form. This was justice in the West—harsh, swift, and relentless. The bounty would pay. But at what cost, he wondered?

By dawn, Caleb “Coyote” Grady and Daisy were already on the road back to Prescott Flats. A proud, orange sun rose at their backs, casting long shadows across the dusty landscape. Another long day awaited, another journey, and somewhere else, another lost soul who needed tracking down.

This was the Wild West—where every sunrise promised the thrill of dusty trails and the thunder of gunfire, and every sunset spelled the end of legends, real or imagined.
```

**Generated Output**:
```
The old perkins. homestead coupla miles north” the lifeless form this was poured! wordlessly! and looked at? the saloon as caleb holstered his whiskey was on a coyote reminding him of a moment? he could? pull the thrill of whiskey “obliged” he dismounted and crouched by the sky in his throat “he’s been around. reckon! he’s stayin’ up by the. bar a glass of the porch he could pull the trigger! caleb said tipping his way through him savoring the walls casting long shadows across the frontier dust swirled in a wiry drifter after a guitar “evenin’” caleb said dropping.

```

---

## Applications

- **Creative Writing**: Mimic the style of specific authors or genres.  
- **Text Simulation**: Generate random text for software testing.  
- **Educational Tool**: Demonstrate how Markov Chains work for students and learners.

---

## Future Enhancements

- **N-grams**: Add support for multi-word sequences to improve context and coherence.
- **Interactive Interface**: Build a GUI for easier interaction.  
- **Real-Time Training**: Allow users to input text directly or train with multiple files simultaneously.  
- **Save/Load Model**: Implement functionality to save the Markov Chain graph for reuse.

---

**Explore the power of Markov Chains and generate creative text with this simple yet effective tool!**
