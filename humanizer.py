import random
import re

# Simple dictionary for word replacements to sound more casual
SYNONYMS = {
    'however': 'but',
    'therefore': 'so',
    'utilize': 'use',
    'demonstrate': 'show',
    'numerous': 'many',
    'subsequent': 'next',
    'approximate': 'rough',
    'thereby': 'thus',
    'methodology': 'method',
    'conceptualize': 'imagine',
}

FILLER_PHRASES = [
    'I guess',
    'kind of',
    'honestly',
    'maybe',
    'you know',
]

def humanize_text(text: str) -> str:
    """Convert formal text to a slightly more casual style."""
    # Replace words using the synonym dictionary
    def replace(match):
        word = match.group(0)
        lower = word.lower()
        if lower in SYNONYMS:
            replacement = SYNONYMS[lower]
            # Preserve capitalization
            if word[0].isupper():
                replacement = replacement.capitalize()
            return replacement
        return word

    # Basic word replacement
    text = re.sub(r'\b\w+\b', replace, text)

    # Optionally insert filler phrases between sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    humanized = []
    for sentence in sentences:
        humanized.append(sentence)
        if sentence and random.random() < 0.3:
            humanized.append(random.choice(FILLER_PHRASES))
    return ' '.join(humanized)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Humanize formal text")
    parser.add_argument('text', nargs='*', help='Text to humanize')
    args = parser.parse_args()
    input_text = ' '.join(args.text) if args.text else input('Enter text: ')
    print(humanize_text(input_text))


if __name__ == '__main__':
    main()
