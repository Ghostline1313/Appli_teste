[app]

# (str) Titre de votre application
title = Mon Application

# (str) Nom du package
package.name = monapplication

# (str) Domaine du package (nécessaire pour l'emballage android/ios)
package.domain = org.test

# (str) Répertoire du code source où se trouve le main.py
source.dir = .

# (list) Extensions de fichiers source à inclure (laisser vide pour inclure tous les fichiers)
source.include_exts = py,png,jpg,kv,atlas

# (list) Liste des inclusions utilisant la correspondance de motifs
#source.include_patterns = assets/*,images/*.png

# (list) Fichiers source à exclure (laisser vide pour ne rien exclure)
#source.exclude_exts = spec

# (list) Liste de répertoires à exclure (laisser vide pour ne rien exclure)
#source.exclude_dirs = tests, bin

# (str) Version de l'application (méthode 1)
version = 0.1

# (list) Exigences de l'application
requirements = python3,kivy,kivymd,plyer

# (str) Répertoires source personnalisés pour les exigences
#requirements.source =

# (list) Exigences de Garden
#garden_requirements =

# (str) Presplash de l'application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icône de l'application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Orientation supportée (l'une des suivantes : landscape, portrait ou all)
orientation = portrait

# (list) Liste des services à déclarer
#services = NAME:ENTRYPOINT_TO_PYTHON_FILE

# (str) Filtres logcat Android
#android.logcat_filters = *:S python:D

# (bool) Copier la bibliothèque au lieu de faire un libs.so
#android.copy_libs = 1

# (str) Version du NDK Android à utiliser (par défaut 19b)
#android.ndk = 19b

# (int) Version de l'API Android à utiliser (par défaut 27)
#android.api = 27

# (int) API minimum requise (par défaut 21)
#android.minapi = 21

# (int) Version du SDK Android à utiliser (par défaut 27)
#android.sdk = 27

# (str) Répertoire du NDK Android (s'il est vide, il sera automatiquement téléchargé)
#android.ndk_path =

# (str) Répertoire du SDK Android (s'il est vide, il sera automatiquement téléchargé)
#android.sdk_path =

# (str) Branche python-for-android à utiliser
#p4a.branch = master

# (str) Catégorie de la console OUYA. Doit être l'une des suivantes : GAME ou APP
#ouya.category = GAME

# (str) L'arch Android à construire, choix : armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (int) Version de l'API NDK Android à utiliser. C'est l'API minimum que votre application supportera, elle devrait généralement correspondre à android.minapi.
#android.ndk_api = 21

# (bool) Sélectionner si activer ou désactiver le shim de compatibilité AndroidX.
#android.enable_androidx = True

# (bool) Utiliser la structure de projet Android Studio (True) ou la structure ant héritée (False)
#android.use_android_studio = True

# (str) Les filtres logcat Android à utiliser
#android.logcat_filters = *:S python:D

# (str) L'arch Android à construire, choix : armeabi-v7a, arm64-v8a, x86, x86_64
#android.arch = armeabi-v7a

# (int) L'API Android à utiliser
#android.api = 27

# (int) L'API Android minimum à supporter
#android.minapi = 21

# (int) L'API Android cible à utiliser
#android.targetapi = 27

# (str) La version du NDK Android à utiliser
#android.ndk = 19b

# (str) La version du SDK Android à utiliser
#android.sdk = 27

# (str) Le répertoire du NDK Android à utiliser
#android.ndk_path =

# (str) Le répertoire du SDK Android à utiliser
#android.sdk_path =

# (str) L'URL git de python-for-android à cloner
#p4a.source_dir =

# (str) La branche de python-for-android à utiliser
#p4a.branch = master

# (str) Le répertoire de clone git de python-for-android (s'il est vide, il sera automatiquement cloné)
#p4a.local_dir =

# (str) L'exigence à utiliser pour python-for-android
#p4a.requirement =

# (str) Le bootstrap de python-for-android à utiliser (par défaut sdl2)
#p4a.bootstrap = sdl2

# (int) numéro de port pour spécifier un argument --port= p4a explicite (par exemple pour bootstrap flask)
#p4a.port =

# (str) Le fichier de liste blanche de python-for-android à utiliser
#p4a.whitelist =

# (str) Le fichier de liste noire de python-for-android à utiliser
#p4a.blacklist =

# (str) La recette par défaut de python-for-android à utiliser
#p4a.default_recipe = sdl2

# (str) Le mode de construction de python-for-android à utiliser (debug, release)
#p4a.build_mode = debug

# (str) Le répertoire de sortie de construction de python-for-android à utiliser
#p4a.build_output = builds

# (str) Le nom de l'apk de sortie de construction de python-for-android à utiliser
#p4a.build_output_apk_name = myapp

# (str) Le répertoire de sortie de construction de l'apk de python-for-android à utiliser
#p4a.build_output_apk_dir = bin

# (str) Le nom de fichier de l'apk de sortie de construction de python-for-android à utiliser
#p4a.build_output_apk_filename = myapp.apk

# (str) Le chemin de l'apk de sortie de construction de python-for-android à utiliser
#p4a.build_output_apk_path = bin/myapp.apk

# (str) Le nom de fichier de l'apk de sortie de construction de python-for-android buildozer à utiliser
#p4a.build_output_apk_buildozer_filename = myapp-buildozer.apk

# (str) Le chemin de l'apk de sortie de construction de python-for-android buildozer à utiliser
#p4a.build_output_apk_buildozer_path = bin/myapp-buildozer.apk

# (str) Le nom de fichier de l'apk de sortie de construction de python-for-android buildozer debug à utiliser
#p4a.build_output_apk_buildozer_debug_filename = myapp-buildozer-debug.apk

# (str) Le chemin de l'apk de sortie de construction de python-for-android buildozer debug à utiliser
#p4a.build_output_apk_buildozer_debug_path = bin/myapp-buildozer-debug.apk

# (str) Le nom de fichier de l'apk de sortie de construction de python-for-android buildozer release à utiliser
#p4a.build_output_apk_buildozer_release_filename = myapp-buildozer-release.apk

# (str) Le chemin de l'apk de sortie de construction de python-for-android buildozer release à utiliser
#p4a.build_output_apk_buildozer_release_path = bin/myapp-buildozer-release.apk

# (str) Le nom de fichier de l'apk de sortie de construction de python-for-android buildozer debug non signé à utiliser
#p4a.build_output_apk_buildozer_debug_unsigned_filename = myapp-buildozer-debug-unsigned.apk

# (str) Le chemin de l'apk de sortie de construction de python-for-android buildozer debug non signé à utiliser
#p4a.build_output_apk_buildozer_debug_unsigned_path = bin/myapp-buildozer-debug-unsigned.apk

# (str) Le nom de fichier de l'apk de sortie de construction de python-for-android buildozer release non signé à utiliser
#p4a.build_output_apk_buildozer_release_unsigned_filename = myapp-buildozer-release-unsigned.apk

# (str) Le chemin de l'apk de sortie de construction de python-for-android buildozer release non signé à utiliser
#p4a.build_output_apk_buildozer_release_unsigned_path = bin/myapp-buildozer-release-unsigned.apk

# (str) Le nom de fichier de l'aab de sortie de construction de python-for-android à utiliser
#p4a.build_output_aab_filename = myapp.aab

# (str) Le chemin de l'aab de sortie de construction de python-for-android à utiliser
#p4a.build_output_aab_path = bin/myapp.aab

# (str) Le nom de fichier de l'aab de sortie de construction de python-for-android buildozer à utiliser
#p4a.build_output_aab_buildozer_filename = myapp-buildozer.aab

# (str) Le chemin de l'aab de sortie de construction de python-for-android buildozer à utiliser
#p4a.build_output_aab_buildozer_path = bin/myapp-buildozer.aab

# (str) Le nom de fichier de l'aab de sortie de construction de python-for-android buildozer debug à utiliser
#p4a.build_output_aab_buildozer_debug_filename = myapp-buildozer-debug.aab

# (str) Le chemin de l'aab de sortie de construction de python-for-android buildozer debug à utiliser
#p4a.build_output_aab_buildozer_debug_path = bin/myapp-buildozer-debug.aab

# (str) Le nom de fichier de l'aab de sortie de construction de python-for-android buildozer release à utiliser
#p4a.build_output_aab_buildozer_release_filename = myapp-buildozer-release.aab

# (str) Le chemin de l'aab de sortie de construction de python-for-android buildozer release à utiliser
#p4a.build_output_aab_buildozer_release_path = bin/myapp-buildozer-release.aab

# (str) Le nom de fichier de l'aab de sortie de construction de python-for-android buildozer debug non signé à utiliser
#p4a.build_output_aab_buildozer_debug_unsigned_filename = myapp-buildozer-debug-unsigned.aab

# (str) Le chemin de l'aab de sortie de construction de python-for-android buildozer debug non signé à utiliser
#p4a.build_output_aab_buildozer_debug_unsigned_path = bin/myapp-buildozer-debug-unsigned.aab

# (str) Le nom de fichier de l'aab de sortie de construction de python-for-android buildozer release non signé à utiliser
#p4a.build_output_aab_buildozer_release_unsigned_filename = myapp-buildozer-release-unsigned.aab

# (str) Le chemin de l'aab de sortie de construction de python-for-android buildozer release non signé à utiliser
#p4a.build_output_aab_buildozer_release_unsigned_path = bin/myapp-buildozer-release-unsigned.aab
