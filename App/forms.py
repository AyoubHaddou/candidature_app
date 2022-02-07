from flask_wtf import FlaskForm
from wtforms import PasswordField,EmailField,SubmitField,StringField
from wtforms.validators import Length,DataRequired,Email,EqualTo,ValidationError
from .models import Users

class Login(FlaskForm):
    """[Form to login]
    """
    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    password = PasswordField(label="Mot de passe:", validators = [DataRequired()])
    submit = SubmitField(label="Se connecter")


class AddCandidacy(FlaskForm):
    """[Form to add candidacy]
    """
    platform= StringField(label='Plateforme', validators=[DataRequired()])
    job = StringField(label='Poste', validators=[DataRequired()])
    entreprise = StringField(label='Entreprise', validators=[DataRequired()])
    activity = StringField(label="Infos complémentaires", validators=[DataRequired()])
    location = StringField(label='Lieu', validators=[DataRequired()])
    contact_full_name = StringField(label='Nom du contact', validators=[DataRequired()])
    contact_email = StringField(label='Email du contact', validators=[DataRequired()])
    contact_mobilephone = StringField(label='Téléphone du contact')
    submit = SubmitField(label='Ajouter')

class ModifyProfile(FlaskForm):
    """[Form to modify profile]
    """
    email = EmailField(label="Adresse mail:", validators = [DataRequired()])
    current_password = PasswordField(label="Mot de passe actuel:", validators = [DataRequired()])
    new_password = PasswordField(label="Nouveau mot de passe:", validators = [DataRequired()])
    submit = SubmitField(label="Valider")

class ModifyCandidacy(FlaskForm):
    """[form to modify candidacy]
    """
    platform= StringField(label='Plateforme', validators=[DataRequired()])
    job = StringField(label='Poste', validators=[DataRequired()])
    entreprise = StringField(label='Entreprise', validators=[DataRequired()])
    activity = StringField(label="Infos complémentaires", validators=[DataRequired()])
    location = StringField(label='Lieu', validators=[DataRequired()])
    contact_full_name = StringField(label='Nom du contact', validators=[DataRequired()])
    contact_email = StringField(label='Email du contact', validators=[DataRequired()])
    contact_mobilephone = StringField(label='Téléphone du contact')
    status = StringField(label='Status', validators=[DataRequired()])
    
    submit = SubmitField(label="Valider")