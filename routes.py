from flask import Blueprint, request, jsonify , render_template, redirect, request
from models import db, Recipe, Comment, Rating

recipes_bp = Blueprint('recipes', __name__)

@recipes_bp.route("/", methods=["POST"])
def add():
    try:
        name = request.form['name']
        ingredients = request.form['ingredients']
        steps = request.form['steps']
        preparation_time = request.form['preparation_time']
        
        if not name or not ingredients or not steps or not preparation_time:
            return jsonify({"error": "All fields are required."}), 400
        
        new_recipe = Recipe(name=name, ingredients=ingredients, steps=steps, preparation_time=preparation_time)
        db.session.add(new_recipe)
        db.session.commit()
        return redirect('/recipes')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        

@recipes_bp.route("/", methods=[ "GET"])
def get():
    try:
        recipes = Recipe.query.order_by(Recipe.created_at.desc()).all()
        return render_template('index.html', Recipes=recipes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@recipes_bp.route("/delete/<int:id>")
def delete(id:int):
    try:
        delete_recipe = Recipe.query.get_or_404(id)
        db.session.delete(delete_recipe)
        db.session.commit()
        return redirect('/recipes')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@recipes_bp.route("/<int:id>", methods=["GET"])
def get_recipe(id):
    try:
        recipe = Recipe.query.get_or_404(id)
        return jsonify({
            'id': recipe.id,
            'name': recipe.name,
            'ingredients': recipe.ingredients,
            'steps': recipe.steps,
            'preparation_time': recipe.preparation_time
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@recipes_bp.route("/<int:id>", methods=["PUT"])
def update_recipe(id):
    try:
        edit_recipe = Recipe.query.get_or_404(id)
        data = request.json
        edit_recipe.name = data['name']
        edit_recipe.ingredients = data['ingredients']
        edit_recipe.steps = data['steps']
        edit_recipe.preparation_time = data['preparation_time']
        db.session.commit()
        return jsonify({"message": "Successfully updated recipe"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@recipes_bp.route('/<int:recipe_id>/ratings/', methods=['POST'])
def rate_recipe(recipe_id):
    try:
        recipe = Recipe.query.get_or_404(recipe_id)
        rating_value = request.form.get('rate')
        if not rating_value:
            return jsonify({"error": "Rate value is required."}), 400
        new_rating = Rating(rate=rating_value, recipe_id=recipe_id)
        db.session.add(new_rating)
        db.session.commit()
        return redirect(f"/recipes/{recipe_id}/ratings/")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@recipes_bp.route('/<int:recipe_id>/ratings/', methods=['GET'])
def get_ratings(recipe_id):
    try:
        recipe = Recipe.query.get_or_404(recipe_id)
        ratings = Rating.query.filter_by(recipe_id=recipe_id).all()
        ratings_list = [{
            'id': rating.id,
            'rate': rating.rate,
            'recipe_id': rating.recipe_id
        } for rating in ratings]

        recipe_data = {
            'id': recipe.id,
            'name': recipe.name,
            'ingredients': recipe.ingredients,
            'steps': recipe.steps,
            'preparation_time': recipe.preparation_time,
            'created_at': recipe.created_at,
            'ratings': ratings_list
        }
        return render_template('ratings.html', recipe=recipe_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@recipes_bp.route('/<int:recipe_id>/comments/', methods=['GET'])
def get_comments(recipe_id):
    try:
        recipe = Recipe.query.get_or_404(recipe_id)
        comments = Comment.query.filter_by(recipe_id=recipe_id).all()
        comments_list = [{
            'id': comment.id,
            'text': comment.text,
            'recipe_id': comment.recipe_id
        } for comment in comments]
        recipe_data = {
            'id': recipe.id,
            'name': recipe.name,
            'ingredients': recipe.ingredients,
            'steps': recipe.steps,
            'preparation_time': recipe.preparation_time,
            'created_at': recipe.created_at,
            'comments': comments_list
        }
        return render_template('comments.html', recipe=recipe_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@recipes_bp.route('/<int:recipe_id>/comments/', methods=['POST'])
def add_comment(recipe_id):
    try:
        data = request.form
        text = data.get('text')
        if not text:
            return jsonify({"error": "Comment text is required."}), 400
        new_comment = Comment(text=text, recipe_id=recipe_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(f"/recipes/{recipe_id}/comments/")
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@recipes_bp.route("/<int:id>/search/", methods=["GET"])
def search_recipes(id: int):
    try:
        # Retrieve the query parameter from the request
        query = int(request.args.get('query'))
        
        # Perform a case-insensitive search on recipe names
        recipes = Recipe.query.filter(Recipe.id == query).all()
        
        return render_template('search.html', Recipes=recipes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
