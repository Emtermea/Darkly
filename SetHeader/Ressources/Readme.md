Dans la page accessible via le lien du copyright en bas de page,
Les commentaires donnent des indices sur la modification des headers.
Pour obtenir le flag, il faut modifier le User-Agent par "ft_bornToSec" ainsi que le Referer par "https://www.nsa.gov/"
La commande suivante récupère le flag :
`curl -A ft_bornToSec --referer https://www.nsa.gov/ "[IP]/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c" | grep flag`