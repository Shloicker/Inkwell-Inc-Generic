from text_adventure import item, weapon, shield, armour, healing_consumable, currency

iron_sword = weapon("Iron Sword", "A simple but robust sword made from cast iron.", 500, 50)
iron_shield = shield("Iron Shield", "A sturdy shield made from cast iron.", 500, 25)
iron_armour = armour("Iron Armour", "Heavy but highly durable armour made from cast iron.", 1000, 25)
steel_sword = weapon("Steel Sword", "An expertly crafted sword made from steel.", 750, 75)
steel_shield = shield("Steel Shield", "A large but light shield that offers substantial protection.", 750, 45)
steel_armour = armour("Steel Armour", "A suit of armour that is stronger and lighter than that made of cast iron.", 1500, 35)
gold_necklace = item("Gold Necklace", "A light necklace made from pure gold.", 1000)
silver_ring = item("Silver Ring", "A small ring made from silver.", 500)
healing_potion = healing_consumable("Healing Potion", "A basic healing potion.", 250, 50)
spider_poison = healing_consumable("Spider Poison", "Deadly posion that should probably not be consumed.", 100, -50)
rusted_sword = weapon("Rusted Sword", "A weak rusted sword barely holding at the hilt. Its strength must have been somehow linked to its wielder's life force.", 100, 25)
gold = currency("Gold", "Shiny gold with curious engravings.", 1)