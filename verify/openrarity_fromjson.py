import argparse
import os
import time
import json

from open_rarity import (
    Collection,
    Token,
    RarityRanker,
    TokenMetadata,
    StringAttribute,
)
from open_rarity.models.token_identifier import EVMContractTokenIdentifier
from open_rarity.models.token_standard import TokenStandard

parser = argparse.ArgumentParser(description='Calculate open rarity rankings for json folder')
parser.add_argument('-f', '--folder', help='Json folder to calculate rarities', default='./json')
args = parser.parse_args()
INPUT_FOLDER = args.folder

print("folder:", INPUT_FOLDER)

trait_counts = {}
tokens = []
start = time.time()

for filename in os.listdir(INPUT_FOLDER):
    if filename == '.DS_Store':  # Skip macOS .DS_Store files
        continue

    file_path = os.path.join(INPUT_FOLDER, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        nft = json.load(f)

    tokenId = filename if not filename.endswith('.json') else filename[:-5] 

    attributes = []
    if 'attributes' in nft and nft['attributes'] is not None:
        attributes = nft['attributes']
    if 'properties' in nft and nft['properties'] is not None and len(attributes) == 0:
        attributes = nft['properties']

    if attributes == None or len(attributes) == 0:
        print("attributes not defined: ", tokenId)
        continue
    try:
        trait_type_used = []
        for attribute in attributes:
            type = str(attribute['trait_type'])
            value = str(attribute['value'])
            if type in trait_type_used:
                continue # don't record duplicate attributes
            if type not in trait_counts:
                trait_counts[type] = {}
            if value not in trait_counts[type]:
                trait_counts[type][value] = 0

            trait_counts[type][value] += 1
            trait_type_used.append(type)

        tokens.append(
            Token(
                token_identifier=EVMContractTokenIdentifier(
                    contract_address="0x0", token_id=tokenId
                ),
                token_standard=TokenStandard.ERC721,
                metadata=TokenMetadata(
                    string_attributes= {str(a['trait_type']):StringAttribute(name=str(a['trait_type']), value=str(a['value'])) for a in attributes}
                )
            )
        )
    except Exception as e:
        print(e)
        print("attributes not properly formatted: ", tokenId)

print(len(os.listdir(INPUT_FOLDER)), len(tokens))
stop = time.time()
duration = stop-start
print(trait_counts)
print('duration: ', duration, '\n')

collection = Collection(
    name= "local",
    tokens=tokens
) 

# Generate scores for a collection
ranked_tokens = RarityRanker.rank_collection(collection=collection)

# Iterate over the ranked and sorted tokens
for token_rarity in ranked_tokens:
    token_id = token_rarity.token.token_identifier.token_id
    rank = token_rarity.rank
    score = token_rarity.score
    unique_attributes = token_rarity.token_features.unique_attribute_count
    print(f"\tToken {token_id} has rank {rank} score: {score} unique attributes: {unique_attributes}")

print('\n')