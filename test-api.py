import pokebase as pb
#https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/
# pokemon/versions/generation-v/black-white/animated/4.gif

pokemon = pb.pokemon("charizard")
print(pokemon.height)
print(pokemon.weight)
#print(pokemon.id)
s1 = pb.SpriteResource('pokemon', pokemon.id)
abilities = ""
types = ""
for ability in pokemon.abilities:
  #print(ability.ability.names[5].name)
#  print(ability.ability.effect_entries[1].effect)
  abilities += ability.ability.names[5].name+', '
  print(ability.ability.effect_entries[1].effect)



#    if len(pokemon.abilities) > 1:
#        abilities += ability.ability.name + ', '
#    else:
#        abilities += ability.ability.name
#for poketype in pokemon.types:
  #print(poketype.type.names[5].name)
  #types += poketype.type.name 


#chesto = pb.APIResource('berry', 'chesto')
#chesto.name
#'chesto'
#chesto.natural_gift_type.name
#'water'
#charmander = pb.pokemon('charmander')  # Quick lookup.
#charmander.height
# Now with sprites! (again!)
#s1 = pb.SpriteResource('pokemon', 17)
#<pokebase.interface.SpriteResource object at 0x7f2f15660860>
#s1.url
#'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png'
#s2 = pb.SpriteResource('pokemon', 1, other=True, official_artwork=True)
#s2.path
#'/home/user/.cache/pokebase/sprite/pokemon/other-sprites/official-artwork/1.png'
#s3 = pb.SpriteResource('pokemon', 3, female=True, back=True)
#s3.img_data
#b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 ... \xca^\x7f\xbbd*\x00\x00\x00\x00IEND\xaeB`\x82'