using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class monopatinhambur : MonoBehaviour {
	public GameObject Sam;
	public float tiempo;
	public bool jetPack;
	public bool tiempoJetpack;
	public float time;
	public bool tiempoRayo;
	public float boost;
	public GameObject barraVidaHam;
	float barraEscala;
	public float velocidad;
	public  Rigidbody rb;
	public bool grounded;
	public GameObject marioneta;
	float x;
	float y;
	float z;
	public bool derecha;
	public float vidaHambur;
	AudioSource dañohambur;
	// Use this for initialization

	void Start () {

		dañohambur = GetComponent<AudioSource>();
		time = 4;
		boost = 1;
		barraEscala = -2.5f;
		barraVidaHam.GetComponent<RectTransform>().localScale = new Vector3 (barraEscala,0.2f,0);
		grounded = true;
		velocidad = 0;
		rb = GetComponent<Rigidbody> ();
		derecha = false;
		vidaHambur = 200.00f;
		tiempo = 8;

	}

	void Update () {

		

		
	
		//barra hamburguesa
		//barraVidaHam.GetComponent<>().
		barraVidaHam.GetComponent<RectTransform>().localScale = new Vector3 (barraEscala,0.2f,0);
		barraVidaHam.GetComponent<Image> ().color = new Color (1.0f*(1-(vidaHambur/250)),1.00f*(vidaHambur/250),0);



		//asignacion valores
		x = this.transform.position.x;
		y = this.transform.position.y;
		z = this.transform.position.z;

		//TODO METER QUE NO SE PUEDA HACER DOBLE SALTO.
		//si gr

		if (tiempoRayo == true){
			boost = 3.00f;
			time -= Time.deltaTime;

		}else if (time <= 0){
			tiempoRayo = false;
		}

		if (tiempoRayo == false){
			boost = 1.00f;
		}


		if (grounded == true) {
			if (Input.GetKey (KeyCode.RightArrow) && velocidad * boost == 0 && grounded) {
				velocidad = 0.2f;
				rb.AddForce(velocidad * boost,0,0);

			} else if (Input.GetKey(KeyCode.LeftArrow) && grounded){

				velocidad = -0.2f;
				rb.AddForce(velocidad * boost,0,0);

			}
			else {
				velocidad = 0.0f;
			}
		}

		if (grounded == false) {

			if (Input.GetKey (KeyCode.RightArrow) ) {
				velocidad = 0.1f;
				rb.AddRelativeForce(velocidad * boost,0,0);

			} else if (Input.GetKey(KeyCode.LeftArrow)){
				velocidad = -0.1f;
				rb.AddRelativeForce(velocidad * boost,0,0);

			}


		}


		this.transform.Translate (0, 0, velocidad * boost);

		if (Input.GetKeyDown (KeyCode. UpArrow) && grounded) {
			rb.AddForce (0, 500.00f, 0);
		}

		//limites
		if (this.transform.position.z < -14.58f){			
			this.transform.position = new Vector3(x,y,-14.00f);
			rb.AddForce (00.0f,00.0f,100.0f);			
		}
		if (this.transform.position.z >14.85f){
			this.transform.position = new Vector3(x,y,14.5f);
			rb.AddForce (00.0f,00.0f,-100.0f);
		}
		

		
		if (tiempoJetpack == false && Input.GetKey(KeyCode.UpArrow)) {
			rb.AddForce (0, 0, 0);
			
		}

		if (Input.GetKey (KeyCode.UpArrow) && jetPack && tiempoJetpack) {
			rb.AddForce (0, 30.00f, 0);
			tiempo -= Time.deltaTime;

		} else if (tiempo <= 0) {
			tiempoJetpack = false;
		
		}


	}


	void OnTriggerEnter (Collider otro){
		if (otro.tag == "JetPack") {
			jetPack = true;
			tiempoJetpack = true;
		
		
		} else if (tiempo <= 0) {
			tiempoJetpack = false;
		}

		if (otro.tag =="rayo"){
			tiempoRayo = true;

		}else if (time <= 0) {
			tiempoRayo = false;
		}

		if (otro.tag == "balasamurai") {
			vidaHambur -= 10;
			barraEscala = -2.5f * (vidaHambur/250.0f);
			dañohambur.Play();
		
		}

		if (otro.tag == "melesamurai") {
			vidaHambur -= 50;
			barraEscala = -2.50f * (vidaHambur/250.0f);
			dañohambur.Play();
		
		}

		if (vidaHambur <= 0) {
			barraEscala = 0.1f;
			barraVidaHam.GetComponent<RectTransform>().localScale = new Vector3 (barraEscala,0.01f,0);
			
			this.gameObject.SetActive(false);
			Invoke("CargarNivel3",3);

		
		}
	
	}
	void CargarNivel3(){
		SceneManager.LoadScene(3);
	}


	void OnTriggerStay(Collider otro) {
		if(otro.tag == "grounded"){
			grounded = true;
		}

	} 
	void OnTriggerExit(Collider otro){
		if (otro.tag == "grounded") {
			grounded = false;
		}

		//if (Input.GetKey ("d")) {
		//velocidad = 0.1f;
		//rb.AddRelativeForce(velocidad,0,0);

		//} else if (Input.GetKey("a")){
		//velocidad = -0.1f;
		//rb.AddRelativeForce(velocidad,0,0);

	}

	
	
}