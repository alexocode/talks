defmodule BlogTest do
  use ExUnit.Case

  describe ".comments_for_article with a non-existing article" do
    test "returns an error" do
      assert {:error, _details} = Blog.comments_for_article(nil)
    end
  end

  describe ".comments_for_article with a new article" do
    setup context do
      [article: insert_article()]
    end

    test "returns no comments", context do
      {:ok, comments} = Blog.comments_for_article(context.article)

      assert length(comments) == 0
    end
  end

  describe ".comments_for_article with an article with 10 comments" do
    setup context do
      article = insert_article()
      
      for _ <- 1..10, do: insert_comment_for_article(article)

      [article: article]
    end

    test "returns 10 comments", context do
      {:ok, comments} = Blog.comments_for_article(context.article)

      assert length(comments) == 10
    end
  end
end