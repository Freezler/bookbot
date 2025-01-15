<<<<<<<<<<<<<<  ✨ Codeium Command 🌟 >>>>>>>>>>>>>>>>
 def fight_soldiers(soldier_one, soldier_two):
+    soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
+    soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
 
-def get_soldier_dps():
-    soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"],soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
-
-    get_soldier_dps()
     if soldier_one_dps > soldier_two_dps:
         return "soldier 1 wins"
+    elif soldier_two_dps > soldier_one_dps:
-    if soldier_two_dps > soldier_one_dps:
         return "soldier 2 wins"
+    else:
+        return "both soldiers die"
-    return "both soldiers die"
<<<<<<<  acf5ace5-1f26-4b82-82aa-4aeef5c67c71  >>>>>>>