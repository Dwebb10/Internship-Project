Feature: Secondary deals pagination
  Background:
    Given I open the site
    When I log in

  Scenario: Open Secondary and paginate last -> first
    When I open the Secondary page
    And I go to the final page
    Then I go back to the first page

