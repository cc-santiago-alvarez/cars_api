from flask import jsonify, render_template

def generic_response(data= None, status = 200, message= "OK"):
    return jsonify({
       "data": data,
       "status": status,
       "message": message 
    })

def registerError(app):
    '''
    This function handle different types of 
    errors and render the appropriate error page
    '''
    @app.errorhandler(404)
    def pageNotFound(e):
        errorTitle = "404 Error: Page Not Found :("
        return render_template('errors/error.html', errorTitle=errorTitle), 404

    @app.errorhandler(500)
    def internalServerError(e):
        # return render_template('500.html'), 500
        return jsonify({'message': f'An error has occurred: {e}'}), 500

    @app.errorhandler(403)
    def forbidden(e):
        errorTitle = "403 Error: Forbidden :("
        return render_template('errors/error.html', errorTitle=errorTitle), 403

    @app.errorhandler(401)
    def unauthorized(e):
        errorTitle = "401 Error: Unauthorized :("
        return render_template('errors/error.html', errorTitle=errorTitle), 401

    @app.errorhandler(400)
    def badRequest(e):
        errorTitle = "400 Error: Bad Request :("
        return render_template('errors/error.html', errorTitle=errorTitle), 400
    
   #  @app.errorhandler(TypeError)
   #  def handle_type_error(e):
   #      message = e.args[0] if e.args else str(e)
   #      # return render_template('500.html'), 500
   #      return jsonify({'message': f'A TypeError has occurred: {message}'}), 500
    
   #  @app.errorhandler(Exception)
   #  def exception(e):
   #      return jsonify({'message': f'An error has occurred: {e}'}), 500