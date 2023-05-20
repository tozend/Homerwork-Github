EXISTING_REPO_NAME = 'Python'
PER_PAGE_MAXIMUM = 100


def test_search_topic_positive(fixture_github_api_client):
    """
    This test search for repos with existing topic on GitHub
    """
    # Search for topics with existing name
    topics_list = fixture_github_api_client.search_topics(EXISTING_REPO_NAME)

    # Validate if repos with given topic exists
    assert topics_list


def test_search_topic_negative(fixture_github_api_client):
    """
    This test search for repos with non-existing topic on GitHub
    """
    # Prepare the non-existing repo name
    topic_name = "Python895yc3498ucm983u938u4d5984ud859u438d95u8"

    # Search for topics for given topic name
    topics_list = fixture_github_api_client.search_topics(topic_name)

    # Validate if repos with given topic cannot be found
    assert not topics_list


def test_search_topic_per_page(fixture_github_api_client):
    """
    This test checks if per page parameter actually changes number of results
    """
    # Search for topics with existing name, with per_page parameter added
    topics_list = fixture_github_api_client.search_topics(EXISTING_REPO_NAME, per_page=50)

    # Validate if repos list have exactly the same amount as in per_page
    assert len(topics_list) == 50


def test_search_topic_per_page_max(fixture_github_api_client):
    """
    This test checks if per page parameter returns max available number of results
    """
    # Search for topics with existing name, with per_page parameter added
    topics_list = fixture_github_api_client.search_topics(EXISTING_REPO_NAME, per_page=PER_PAGE_MAXIMUM)

    # Validate if repos list have exactly the same amount as in per_page
    assert len(topics_list) == PER_PAGE_MAXIMUM


def test_search_topic_per_page_over_limit(fixture_github_api_client):
    """
    This test checks if per page parameter doesn't return number of results more than maximum limit
    """
    # Search for topics with existing name, with per_page parameter added
    topics_list = fixture_github_api_client.search_topics(EXISTING_REPO_NAME, per_page=PER_PAGE_MAXIMUM + 1)

    # Validate if repos list cannot reach more than maximum amount of per_page limitation
    assert len(topics_list) == PER_PAGE_MAXIMUM


def test_search_topic_page(fixture_github_api_client):
    """
    This test checks if repos with different page numbers have different results
    """
    # Search for topics with existing name, for two separate pages
    topics_list_page_1 = fixture_github_api_client.search_topics(EXISTING_REPO_NAME, page=1)
    topics_list_page_2 = fixture_github_api_client.search_topics(EXISTING_REPO_NAME, page=2)

    # Validate if repos with different page numbers have different results
    assert topics_list_page_1 != topics_list_page_2
