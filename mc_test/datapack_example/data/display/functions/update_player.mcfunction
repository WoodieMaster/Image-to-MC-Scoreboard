execute store result score @s selected_slot run data get entity @s SelectedItemSlot

execute unless score @s selected_slot = @s last_selected_slot run function display:update_img with entity @s SelectedItem

scoreboard players operation @s last_selected_slot = @s selected_slot