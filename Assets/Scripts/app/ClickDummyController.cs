using TMPro;
using UnityEngine;

namespace app
{
    public class ClickDummyController : MonoBehaviour
    {
        [SerializeField] private TMP_Text label;
        [SerializeField] private GameObject panel;


        public void OnButtonVal1Clicked()
        {
            label.text = "Val1";
        }

        public void OnButtonVal2Clicked()
        {
            label.text = "Val2";
        }
        
        public void OnButtonOpenPanelClicked()
        {
            panel.SetActive(true);
        }

        public void OnButtonClosePanelClicked()
        {
            panel.SetActive(false);
        }
    }
}