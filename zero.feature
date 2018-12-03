Feature: Test of car dealer site

 	Background: log in
	  Given the page "http://salon.rpgit.pl/" is loaded
	  When I type "lina" in "id_username" input
	  And I type "Welcome1" in "id_password" input
	  When I click "id_login_btn" button
	  Then the home page is displayed

	Scenario: add a new car
	  When I click "add-new-car" button
	  And I select "Audi" from "id_marka" select
	  And I type "R8" in "id_model" input
	  And I type "2016" in "id_rocznik" input
	  And I click Zapisz
	  Then there is a car: brand "Audi", model "R8", year "2016"

	Scenario Outline: add new cars
	  When I click "add-new-car" button
	  And I select "<brand>" from "id_marka" select
	  And I type "<model>" in "id_model" input
	  And I type "<year>" in "id_rocznik" input
	  And I click Zapisz
	 Then there is a car: brand "<brand>", model "<model>", year "<year>"

	  Examples:
	      | brand	| model    | year |
	      | Audi    | A1 	   | 2012 |
	      | Audi	| Q3	   | 2010 |
	      | Hyundai | i40 	   | 2011 |
	      | Hyundai | i30	   | 2013 |

	Scenario: clear data
	  When I clear all data
	  Then the table is empty
	  