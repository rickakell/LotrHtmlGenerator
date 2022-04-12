class Card:
    def __init__(self, cardInfoList):
        from re import sub
        from unidecode import unidecode
        self.ID = cardInfoList[0]
        self.rawName = cardInfoList[1]
        self.Name = sub(" ?\(.*\)","",cardInfoList[1])
        self.plainName = unidecode(self.rawName)
        self.D1 = cardInfoList[2]
        self.D2 = cardInfoList[3]
        self.D3 = cardInfoList[4]
        self.D4 = cardInfoList[5]
        self.Sphere = cardInfoList[6]
        self.Type = cardInfoList[7]
        self.Cost = cardInfoList[8]
        self.Threat = cardInfoList[9]
        self.WP = cardInfoList[10]
        self.Att = cardInfoList[11]
        self.Def = cardInfoList[12]
        self.HP = cardInfoList[13]
        self.Traits = cardInfoList[14]
        self.Keyword = cardInfoList[15]
        self.Unique = cardInfoList[16]
        self.Count = cardInfoList[17]
        self.CardText = cardInfoList[18]
        self.Notes = cardInfoList[19]
        self.OwnedYN = cardInfoList[20]
        self.OwnedCount = cardInfoList[21]
        self.SetAndCardID = cardInfoList[22]
        self.Set = cardInfoList[23]
        self.CardNumber = cardInfoList[24]
        self.Cycle = cardInfoList[25]
        self.SetID = cardInfoList[26]
        self.Link = cardInfoList[27]

    def GenerateHtmlString(self):
        return f"""<html>
<title>{self.Name} ({self.Sphere} {self.Type})</title>
<body>
<h1>{self.Name} ({self.Sphere} {self.Type})</h1>


<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column {{"width":"22.22%"}} -->
<div class="wp-block-column" style="flex-basis:22.22%"><!-- wp:image {{"id":3018,"sizeSlug":"large","linkDestination":"none"}} -->
<figure class="wp-block-image size-large"><img src="https://cardtalk2018.files.wordpress.com/2021/04/aragorn-2.jpg?w=429" alt="" class="wp-image-3018"/></figure>
<!-- /wp:image --></div>
<!-- /wp:column -->

<!-- wp:column {{"width":"33.33%"}} -->
<div class="wp-block-column" style="flex-basis:33.33%"><!-- wp:heading {{"level":3}} -->
<h3 id="stats">Stats</h3>
<!-- /wp:heading -->

<!-- wp:table -->
<figure class="wp-block-table"><table><tbody><tr><td>Cost</td><td>{self.Cost}</td></tr><tr><td>Willpower</td><td>{self.WP}</td></tr><tr><td>Attack</td><td>{self.Att}</td></tr><tr><td>Defense</td><td>{self.Def}</td></tr><tr><td>Hit Points</td><td>{self.HP}</td></tr></tbody></table></figure>
<!-- /wp:table --></div>
<!-- /wp:column -->

<!-- wp:column {{"width":"44.45%"}} -->
<div class="wp-block-column" style="flex-basis:44.45%"><!-- wp:heading {{"level":4}} -->
<h4 id="trait-s">Trait(s)</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{self.Traits}</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":4}} -->
<h4 id="keyword-s">Keyword(s)</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{self.Keyword}</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":4}} -->
<h4 id="card-text">Card Text</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{self.CardText}</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

</body>
</html>
"""
    
    def writeHtmlFile(self):
        fileName = f"{self.plainName}.html"
        print(f"Generating {fileName}...")
        with open(f"html/{fileName}", "w+", encoding="ANSI") as file:
            file.writelines(self.GenerateHtmlString())
