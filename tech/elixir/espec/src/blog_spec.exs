defmodule BlogSpec do
  use ESpec

  describe ".comments_for_article" do
    let comments_result: Blog.comments_for_article(article())

    let_ok comments: comments_result()

    context "for a non-existing article" do
      let article: nil

      it "should return an error tuple" do
        comments_result() |> should(be_error_result())
      end
    end

    context "for a new article" do
      let article: insert_article()

      it "should return no comments" do
        comments() |> should(be_empty())
      end
    end

    context "for an article with 10 comments" do
      let article: insert_article()

      before do
        for _ <- 1..10, do: insert_comment_for_article(article())
      end

      it "should return 10 comments" do
        comments() |> should(have_count 10)
      end
    end
  end
end