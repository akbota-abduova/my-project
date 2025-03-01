import os
text = [
    "The sun dipped below the horizon, casting a golden glow over the city.\n",
    "A soft breeze rustled the leaves, carrying the scent of fresh blossoms.\n",
    "Birds chirped their evening songs as they nestled into their homes.\n",
    "A young woman sat by the window, her eyes fixed on the pages of a novel.\n",
    "In the distance, laughter echoed from a small group of children playing.\n",
    "The streetlights flickered on, illuminating the quiet sidewalks.\n",
    "A gentle drizzle began to fall, leaving tiny droplets on the windowpane.\n",
    "A cat curled up on a doorstep, purring softly in the cool air.\n",
    "Music drifted from an open café, blending with the sounds of the night.\n",
    "As midnight approached, the city slowed, wrapped in a peaceful silence.\n"
]

t = ' '.join(text)

with open('new.txt', 'w', encoding='utf-8') as file:
    file.write(t)


print(t) 