using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class monopatin : MonoBehaviour {
	public GameObject HAm;
	public bool tiempoJetpack;
	public bool jetPack;
	public float tiempo;
	public bool tiempoRayo;
	public float time;
	public GameObject barraVidaSam;
	float barraEscala;
	public float velocidad;
	public Rigidbody rb;
	public bool grounded;
	public GameObject marioneta;
	float x;
	float y;
	float z;
	public bool derecha;
	public float boost;
	public float vidaSamurai;
	public GameObject hijo;
	public Animator anim;
	public bool transporter;
	AudioSource daño;

	// Use this for initialization
	void Start () {

		daño = GetComponent<AudioSource>();
		jetPack = false;
		time = 4;
		grounded = true;
		velocidad = 0;
		rb = GetComponent<Rigidbody>();
		derecha = false;
		boost = 1.00f;
		vidaSamurai = 100;
		barraEscala = -8.5f;
		barraVidaSam.GetComponent<RectTransform>().localScale = new Vector3 (barraEscala,0.2f,0);
		hijo = GameObject.Find("PERSONAJE VIDEOJUEGO UNITY");
		//hijo.GetComponent<anim>.SetBoolean correr = false;
		tiempo = 8;

	}
	void Update () {

		/*if (HAm.GetComponent<monopatinhambur>().vidaHambur <= 10.00f){
			SceneManager.LoadScene(3);
		}*/
		

		barraVidaSam.GetComponent<RectTransform>().localScale = new Vector3 (barraEscala,0.2f,0);
		barraVidaSam.GetComponent<Image> ().color = new Color (1.0f*(1-(vidaSamurai/100)),1.00f*(vidaSamurai/100),0);
		x = this.transform.position.x;
		y = this.transform.position.y;
		z = this.transform.position.z;
		if(transporter == true && Input.GetKey(KeyCode.Space)){
			this.transform.position = new Vector3(-9.603f,9.827f,9.05f);
		}
		//TODO METER QUE NO SE PUEDA HACER DOBLE SALTO.
		//si gr
		if (grounded == true) {
			if (Input.GetKey ("d") && velocidad * boost == 0 && grounded) {
				velocidad = 0.2f;
				rb.AddForce(velocidad * boost,0,0);
			} else if (Input.GetKey("a") && grounded){
				velocidad = -0.2f;
				rb.AddForce(velocidad * boost,0,0);
			}
			else {
				velocidad = 0.0f;
			}
		}
		if (grounded == false) {
			if (Input.GetKey ("d") ) {
				velocidad = 0.1f;
				
				rb.AddRelativeForce(velocidad * boost,0,0);
			} else if (Input.GetKey("a") ){
				velocidad = -0.1f;
				
				rb.AddRelativeForce(velocidad * boost,0,0);
			}else {
				
			}
		}
		this.transform.Translate (0, 0, velocidad * boost);
		if (Input.GetKeyDown ("w") && grounded) {
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
		if (tiempoRayo == false){
			boost = 1.00f;
		}

		if (tiempoRayo == true){
			boost = 3.00f;
			time -= Time.deltaTime;

		}else if (time <= 0){
			tiempoRayo = false;
		}

		if (tiempoJetpack == false && Input.GetKey("w")) {
			rb.AddForce (0, 0, 0);
			
		}

		if (Input.GetKey ("w") && jetPack && tiempoJetpack) {
			rb.AddForce (0, 150.00f, 0);
			tiempo -= Time.deltaTime;

		} else if (tiempo <= 0) {
			tiempoJetpack = false;
		
		}
	}
	void OnTriggerStay(Collider otro) {

		if(otro.tag == "teletransportador"){
			transporter = true;

		}
		if(otro.tag == "grounded"){
			grounded = true;
		}
		
	} 
	void OnTriggerExit(Collider otro){
		if (otro.tag == "grounded") {
			grounded = false;
		}
		if(otro.tag == "teletransportador"){
			transporter = false;
		}
	}
	void OnTriggerEnter(Collider otro){
		if (otro.tag =="rayo"){
			tiempoRayo = true;

		}else if (time <= 0) {
			tiempoRayo = false;
		}
		if (otro.tag == "balahamburguesa"){
			vidaSamurai -= 20;
			barraEscala = -8.5f * (vidaSamurai/100.0f);
			daño.Play();
		}
		if (vidaSamurai <= 0) {
			this.gameObject.SetActive(false);
			Invoke("CargarNivel3",3);
			barraEscala = -0.1f;
			barraVidaSam.GetComponent<RectTransform>().localScale = new Vector3 (barraEscala,0.01f,0);
		}
		if (otro.tag == "melehambur") {
			vidaSamurai -= 15;
			barraEscala = -8.50f * (vidaSamurai/100.0f);
			daño.Play();
		}
		if (otro.tag == "JetPack") {
			jetPack = true;
			tiempoJetpack = true;
		} else if (tiempo <= 0) {
			tiempoJetpack = false;
		}
		

	}
	void CargarNivel3(){
		SceneManager.LoadScene(3);
	}

}
